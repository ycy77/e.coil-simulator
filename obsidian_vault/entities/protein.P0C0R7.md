---
entity_id: "protein.P0C0R7"
entity_type: "protein"
name: "rlmE"
source_database: "UniProt"
source_id: "P0C0R7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rlmE ftsJ mrsF rrmJ b3179 JW3146"
---

# rlmE

`protein.P0C0R7`

## Static

- Type: `protein`
- Source: `UniProt:P0C0R7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Specifically methylates the uridine in position 2552 of 23S rRNA at the 2'-O position of the ribose in the fully assembled 50S ribosomal subunit. {ECO:0000269|PubMed:10748051}. RlmE is the methyltransferase responsible for methylation of 23S rRNA at the 2'-O position of the ribose at the universally conserved U2552 nucleotide . In vitro, the enzyme is active on ribosomes and the 50S ribosomal subunit, but not free rRNA . The 45S ribosomal subunit precursor that accumulates in an rlmE mutant is a true intermediate on the pathway of 50S subunit assembly. 2'-O-methylation of U2552 promotes association between helices 92 and 71 of 23S rRNA; together with incorporation of EG11232-MONOMER, it promotes late steps of 50S ribosomal subunit assembly . Cryo-EM structures and biochemical assays show that 2'-O-methylation of U2552 plays a role in ribosome biogenesis and protein translation . A crystal structure of RlmE has been solved at 1.5 Å resolution . Site-directed mutagenesis has identified possible active site and substrate binding residues, and a reaction mechanism has been proposed . A mutant strain lacking RlmE has a decreased growth rate at all temperatures tested and shows reduced protein synthesis activity and accumulation of free ribosomal subunits and assembly intermediates that are unstable at low Mg2+ concentrations...

## Biological Role

Catalyzes RXN-11845 (reaction.ecocyc.RXN-11845).

## Annotation

FUNCTION: Specifically methylates the uridine in position 2552 of 23S rRNA at the 2'-O position of the ribose in the fully assembled 50S ribosomal subunit. {ECO:0000269|PubMed:10748051}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11845|reaction.ecocyc.RXN-11845]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3179|gene.b3179]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C0R7`
- `KEGG:ecj:JW3146;eco:b3179;ecoc:C3026_17310;`
- `GeneID:86862424;93778802;947689;`
- `GO:GO:0000027; GO:0001510; GO:0005829; GO:0006364; GO:0008650`
- `EC:2.1.1.166`

## Notes

Ribosomal RNA large subunit methyltransferase E (EC 2.1.1.166) (23S rRNA Um2552 methyltransferase) (Cell division protein FtsJ) (rRNA (uridine-2'-O-)-methyltransferase)
