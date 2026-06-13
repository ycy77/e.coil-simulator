---
entity_id: "protein.P0ADR6"
entity_type: "protein"
name: "rlmM"
source_database: "UniProt"
source_id: "P0ADR6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rlmM ygdE b2806 JW2777"
---

# rlmM

`protein.P0ADR6`

## Static

- Type: `protein`
- Source: `UniProt:P0ADR6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the 2'-O-methylation at nucleotide C2498 in 23S rRNA. Modifies C2498 in naked 23S rRNA, but not in assembled 50S subunits or ribosomes. {ECO:0000269|PubMed:19400805, ECO:0000269|PubMed:22923526}. RlmM is the methyltransferase responsible for methylation of 23S rRNA at the 2'-O position of the ribose at the C2498 nucleotide within the peptidyl transferase loop. In vitro, the enzyme is active on naked 23S rRNA and unmodified domain V alone , but not assembled 50S ribosomal subunits or ribosomes . Crystal structures of RlmM have been solved , showing the presence of an N-terminal THUMP domain and aC-terminal Rossmann-like fold methyltransferase domain . RlmM was predicted to be an RNA 2'-O-ribose methyltranserase by sequence similarity. The extended N-terminus may act in target recognition . Phylogenetic analysis of this protein family has been performed . Phylogenetic profiling shows an unexplained link between RlmM and RdgC . An rlmM mutant has a slightly longer doubling time in rich medium than wild type and is slowly out-competed by wild type in a growth competition experiment . A knockout of rlmM in combination with rluE was viable at both 37 and 20°C but resulted in large defects on ribosome assembly and peptidyl transferase activity at 20°C . RlmM: "rRNA large subunit methyltransferase M"

## Biological Role

Catalyzes RXN-11589 (reaction.ecocyc.RXN-11589).

## Annotation

FUNCTION: Catalyzes the 2'-O-methylation at nucleotide C2498 in 23S rRNA. Modifies C2498 in naked 23S rRNA, but not in assembled 50S subunits or ribosomes. {ECO:0000269|PubMed:19400805, ECO:0000269|PubMed:22923526}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11589|reaction.ecocyc.RXN-11589]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2806|gene.b2806]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADR6`
- `KEGG:ecj:JW2777;eco:b2806;ecoc:C3026_15425;`
- `GeneID:75172890;75203803;947283;`
- `GO:GO:0005737; GO:0006364; GO:0070677`
- `EC:2.1.1.186`

## Notes

Ribosomal RNA large subunit methyltransferase M (EC 2.1.1.186) (23S rRNA (cytidine2498-2'-O)-methyltransferase) (23S rRNA 2'-O-ribose methyltransferase RlmM)
