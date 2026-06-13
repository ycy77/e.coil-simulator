---
entity_id: "protein.P15288"
entity_type: "protein"
name: "pepD"
source_database: "UniProt"
source_id: "P15288"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pepD pepH b0237 JW0227"
---

# pepD

`protein.P15288`

## Static

- Type: `protein`
- Source: `UniProt:P15288`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Dipeptidase with broad substrate specificity. Requires dipeptide substrates with an unblocked N-terminus and the amino group in the alpha or beta position. Non-protein amino acids and proline are not accepted in the C-terminal position, whereas some dipeptide amides and formyl amino acids are hydrolyzed. Also shows cysteinylglycinase activity, which is sufficient for E.coli to utilize cysteinylglycine as a cysteine source. {ECO:0000269|PubMed:11157967, ECO:0000269|PubMed:20067529, ECO:0000269|PubMed:355237, ECO:0000269|PubMed:7988883}. Peptidase D (PepD) is a dipeptidase capable of breaking down a number of dipeptides with unblocked N termini , including cysteinylglycine, a breakdown product of glutathione . Neither proline nor non-protein amino acids are accepted in the C-terminal position . Transcription of pepD increases five fold during phosphate starvation . Overexpression of pepD negatively affects biofilm formation . Using a method that distinguishes N-phosphorylation from O-phosphorylation, N-phosphorylation was detected in vitro .

## Biological Role

Component of peptidase D (complex.ecocyc.CPLX0-3001).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Dipeptidase with broad substrate specificity. Requires dipeptide substrates with an unblocked N-terminus and the amino group in the alpha or beta position. Non-protein amino acids and proline are not accepted in the C-terminal position, whereas some dipeptide amides and formyl amino acids are hydrolyzed. Also shows cysteinylglycinase activity, which is sufficient for E.coli to utilize cysteinylglycine as a cysteine source. {ECO:0000269|PubMed:11157967, ECO:0000269|PubMed:20067529, ECO:0000269|PubMed:355237, ECO:0000269|PubMed:7988883}.

## Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3001|complex.ecocyc.CPLX0-3001]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0237|gene.b0237]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15288`
- `KEGG:ecj:JW0227;eco:b0237;ecoc:C3026_01125;ecoc:C3026_23860;`
- `GeneID:945013;`
- `GO:GO:0005829; GO:0006508; GO:0008270; GO:0016805; GO:0042803; GO:0043171; GO:0070573`
- `EC:3.4.13.18`

## Notes

Cytosol non-specific dipeptidase (EC 3.4.13.18) (Aminoacyl-histidine dipeptidase) (Beta-alanyl-histidine dipeptidase) (Carnosinase) (Cysteinylglycinase) (Peptidase D) (Xaa-His dipeptidase) (X-His dipeptidase)
