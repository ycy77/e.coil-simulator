---
entity_id: "protein.P30844"
entity_type: "protein"
name: "basS"
source_database: "UniProt"
source_id: "P30844"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "basS pmrB b4112 JW4073"
---

# basS

`protein.P30844`

## Static

- Type: `protein`
- Source: `UniProt:P30844`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system BasS/BasR Autophosphorylates and activates BasR by phosphorylation. {ECO:0000269|PubMed:15522865}. BasS (also known as PmrB) is the sensor histidine kinase of the BasSR two-component system. BasS is a predicted integral membrane protein with sequence similarity to the sensor kinase family of proteins including a conserved histidine (His-152) which is presumed to be the site of autophosphorylation; overproduced BasS autophosphorylates in the presence of ATP and transfers a phosphate to its cognate response regulator, BasR in vitro; it is also able to phosphorylate purified OmpR with low efficiency (see also ). The purified cytoplasmic domain of BasS (Arg-89 → Ile-363) has phospho-BasR phosphatase activity in vitro; variation in the protein phosphatase activity of BasS (PmrB) between E. coli and Salmonella enterica determines the ability of G7172-MONOMER "PmrD" to activate the BasSR (PmrAB) system in the two species . BasSR is required for the Fe(III)-dependent induction of the arnBCADTEF operon; a ΔbasSR strain exhibits mild acid-sensitivity when grown aerobically in medium containing a high (1.5mM) concentration of FeSO4 . basS is upregulated 2.4 fold by growth in 0.2mM ZnSO4 and a ΔbasS strain is hypersensitive to ZnSO4 . BasS is homologous to the well characterized PmrB sensor kinase of Salmonella enterica...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN), RXN0-7339 (reaction.ecocyc.RXN0-7339).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system BasS/BasR Autophosphorylates and activates BasR by phosphorylation. {ECO:0000269|PubMed:15522865}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7339|reaction.ecocyc.RXN0-7339]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4112|gene.b4112]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30844`
- `KEGG:ecj:JW4073;eco:b4112;ecoc:C3026_22220;`
- `GeneID:948632;`
- `GO:GO:0000155; GO:0000160; GO:0004673; GO:0004721; GO:0005524; GO:0005886; GO:0007165; GO:0010041; GO:0010043`
- `EC:2.7.13.3`

## Notes

Sensor protein BasS (EC 2.7.13.3)
