---
entity_id: "protein.Q47083"
entity_type: "protein"
name: "cbl"
source_database: "UniProt"
source_id: "Q47083"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cbl b1987 JW1966"
---

# cbl

`protein.Q47083`

## Static

- Type: `protein`
- Source: `UniProt:Q47083`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: May be an accessory regulatory protein within the cys regulon. The transcription factor Cbl, for "cysB like," is a regulator involved in the expression of genes required for aliphatic sulfonate utilization and homeostatic response to sulfate starvation . Cbl does not require a ligand to bind to its DNA-binding site, but the activity of this protein is negatively regulated by the adenosine 5'-phophosulfate (APS) cofactor . This protein belongs to the large LysR family of transcriptional regulators and it is positively regulated by CysB, which is similar to Cbl (40% identity) . Members of this family have two domains, an N-terminal domain with a helix-turn-helix DNA-binding motif and a large C-terminal domain . In systematic studies of oligomerization, it was shown that some members of the LysR family, like Cbl, interact with other members of the family to form heterodimers, but the physiological significance of this is unknown . The crystal structure of the C-terminal regulatory domain of Cbl (2.8Å) has been solved . The deletion of cbl increased viability in soil , suggesting that the activation of sulfur utilization pathways may be energetically inefficient under nutrient-limited conditions, or that its expression may interfere with more effective pathways for long-term survival...

## Biological Role

Component of Cbl-thiosulfate (complex.ecocyc.CPLX0-9022), Cbl-adenosine 5'-phosphosulfate (complex.ecocyc.MONOMER-2720).

## Annotation

FUNCTION: May be an accessory regulatory protein within the cys regulon.

## Outgoing Edges (11)

- `activates` --> [[gene.b0365|gene.b0365]] `RegulonDB` `S` - regulator=Cbl; target=tauA; function=+
- `activates` --> [[gene.b0366|gene.b0366]] `RegulonDB` `S` - regulator=Cbl; target=tauB; function=+
- `activates` --> [[gene.b0367|gene.b0367]] `RegulonDB` `S` - regulator=Cbl; target=tauC; function=+
- `activates` --> [[gene.b0368|gene.b0368]] `RegulonDB` `S` - regulator=Cbl; target=tauD; function=+
- `activates` --> [[gene.b0933|gene.b0933]] `RegulonDB` `S` - regulator=Cbl; target=ssuB; function=+
- `activates` --> [[gene.b0934|gene.b0934]] `RegulonDB` `S` - regulator=Cbl; target=ssuC; function=+
- `activates` --> [[gene.b0935|gene.b0935]] `RegulonDB` `S` - regulator=Cbl; target=ssuD; function=+
- `activates` --> [[gene.b0936|gene.b0936]] `RegulonDB` `S` - regulator=Cbl; target=ssuA; function=+
- `activates` --> [[gene.b0937|gene.b0937]] `RegulonDB` `S` - regulator=Cbl; target=ssuE; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-9022|complex.ecocyc.CPLX0-9022]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.MONOMER-2720|complex.ecocyc.MONOMER-2720]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b1987|gene.b1987]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47083`
- `KEGG:ecj:JW1966;eco:b1987;ecoc:C3026_11215;`
- `GeneID:946502;`
- `GO:GO:0000976; GO:0003700; GO:0006355; GO:0019344; GO:0045883`

## Notes

HTH-type transcriptional regulator cbl
