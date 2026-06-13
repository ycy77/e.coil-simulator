---
entity_id: "protein.P23003"
entity_type: "protein"
name: "trmA"
source_database: "UniProt"
source_id: "P23003"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trmA b3965 JW3937"
---

# trmA

`protein.P23003`

## Static

- Type: `protein`
- Source: `UniProt:P23003`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Dual-specificity methyltransferase that catalyzes the formation of 5-methyluridine at position 54 (m5U54) in all tRNAs, and that of position 341 (m5U341) in tmRNA (transfer-mRNA). {ECO:0000255|HAMAP-Rule:MF_01011, ECO:0000269|PubMed:23603891, ECO:0000269|PubMed:2999071, ECO:0000269|PubMed:6247318}. TrmA is the methyltransferase that catalyzes methylation of U54 in the TΨ loop of tRNAs as well as methylation of the corresponding U341 residue within the tRNA-like domain of SSRA-RNA . In addition to its catalytic activity, TrmA also acts as a tRNA chaperone . tRNAs carry multiple modifications, often in nearby nucleotide residues. The preferred substrate for the TrmA methyltransferase activity is unmodified tRNA, while its binding activity is highest with Ψ55-modified tRNA . The catalytic mechanism involves formation of a covalent complex between the catalytic Cys324 residue of the enzyme and tRNA and occurs by single SN2 displacement . Stereochemically, the reaction proceeds by cis addition followed by trans elimination . Random and site-directed mutagenesis of conserved residues allowed identification of residues involved in formation of the TrmA-tRNA intermediate, enzymatic activity , as well as SAM and tRNA binding . Glu358 acts as a general base, abstracting a proton from C5 of the methylated reaction intermediate...

## Biological Role

Catalyzes S-adenosyl-L-methionine:tRNA uracil 5-methyltransferase; (reaction.R00594), TRNA-URACIL-5--METHYLTRANSFERASE-RXN (reaction.ecocyc.TRNA-URACIL-5--METHYLTRANSFERASE-RXN).

## Annotation

FUNCTION: Dual-specificity methyltransferase that catalyzes the formation of 5-methyluridine at position 54 (m5U54) in all tRNAs, and that of position 341 (m5U341) in tmRNA (transfer-mRNA). {ECO:0000255|HAMAP-Rule:MF_01011, ECO:0000269|PubMed:23603891, ECO:0000269|PubMed:2999071, ECO:0000269|PubMed:6247318}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00594|reaction.R00594]] `KEGG` `database` - via EC:2.1.1.35
- `catalyzes` --> [[reaction.ecocyc.TRNA-URACIL-5--METHYLTRANSFERASE-RXN|reaction.ecocyc.TRNA-URACIL-5--METHYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3965|gene.b3965]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23003`
- `KEGG:ecj:JW3937;eco:b3965;ecoc:C3026_21425;`
- `GeneID:75203203;947143;`
- `GO:GO:0000049; GO:0005829; GO:0019843; GO:0030488; GO:0030697; GO:0061818`
- `EC:2.1.1.-; 2.1.1.35`

## Notes

tRNA/tmRNA (uracil-C(5))-methyltransferase (EC 2.1.1.-) (EC 2.1.1.35) (tRNA (uracil(54)-C(5))-methyltransferase) (tRNA(m5U54)-methyltransferase) (RUMT) (tmRNA (uracil(341)-C(5))-methyltransferase)
