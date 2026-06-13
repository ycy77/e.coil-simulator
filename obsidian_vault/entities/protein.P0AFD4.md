---
entity_id: "protein.P0AFD4"
entity_type: "protein"
name: "nuoH"
source_database: "UniProt"
source_id: "P0AFD4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nuoH b2282 JW2277"
---

# nuoH

`protein.P0AFD4`

## Static

- Type: `protein`
- Source: `UniProt:P0AFD4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. This subunit may bind ubiquinone. NuoH is part of the inner membrane component of NADH dehydrogenase I . The protein has eight predicted transmembrane domains; the C terminus is located in the periplasm . This subunit was thought to contain the ubiquinone binding site , which has since been proposed to be located in the NuoM subunit . However, an E36Q mutant shows higher apparent Km for ubiquinone, suggesting proximity to the ubiquinone binding domain . The charged residues of the cytoplasmic loops are highly conserved; mutagenesis of these residues results in loss of enzymatic activity and a low content of the peripheral subunits NuoB and NuoCD, indicating that the cytoplasmic loops are essential for assembly of the peripheral arm of NDH-1 . The similarity between NDH-1 and the mitochondrial Complex I has been exploited to study the effects of pathogenic mutations and polymorphisms found in the human proteins on enzymatic activity...

## Biological Role

Catalyzes NADH:ubiquinone oxidoreductase (reaction.R11945). Component of NADH:quinone oxidoreductase I (complex.ecocyc.NADH-DHI-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. This subunit may bind ubiquinone.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R11945|reaction.R11945]] `KEGG` `database` - via EC:7.1.1.2
- `is_component_of` --> [[complex.ecocyc.NADH-DHI-CPLX|complex.ecocyc.NADH-DHI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2282|gene.b2282]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFD4`
- `KEGG:ecj:JW2277;eco:b2282;ecoc:C3026_12735;`
- `GeneID:89517117;93774892;946761;`
- `GO:GO:0005886; GO:0009060; GO:0016020; GO:0016655; GO:0022904; GO:0030964; GO:0045271; GO:0048038; GO:1902600`
- `EC:7.1.1.-`

## Notes

NADH-quinone oxidoreductase subunit H (EC 7.1.1.-) (NADH dehydrogenase I subunit H) (NDH-1 subunit H) (NUO8)
