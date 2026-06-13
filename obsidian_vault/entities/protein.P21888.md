---
entity_id: "protein.P21888"
entity_type: "protein"
name: "cysS"
source_database: "UniProt"
source_id: "P21888"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysS b0526 JW0515"
---

# cysS

`protein.P21888`

## Static

- Type: `protein`
- Source: `UniProt:P21888`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent ligation of cysteine to tRNA(Cys) (PubMed:12662918). Unable to bind serine (PubMed:12662918). {ECO:0000269|PubMed:12662918}.; FUNCTION: In addition to its role as an aminoacyl-tRNA synthetase, has also cysteine persulfide synthase activity. Produces reactive persulfide species such as cysteine persulfide (CysSSH) from substrate cysteine and mediate direct incorporation of CysSSH into proteins during translations, resulting in protein persulfides and polysulfides (PubMed:29079736). CysSSHs behave as potent antioxidants and cellular protectants (PubMed:29079736). {ECO:0000269|PubMed:29079736}. Cysteine-tRNA ligase (CysRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. CysRS belongs to the Class I aminoacyl tRNA synthetases . CysRS is a monomer in solution . The N-terminal domain of CysRS is active in adenylate synthesis, while the C-terminal domain is able to bind and discriminate tRNA. The two domains can not complement each other in trans, showing that full enzymatic activity requires covalent continuity...

## Biological Role

Catalyzes CYSTEINE--TRNA-LIGASE-RXN (reaction.ecocyc.CYSTEINE--TRNA-LIGASE-RXN). Bound by Zinc cation (molecule.C00038).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

FUNCTION: Catalyzes the ATP-dependent ligation of cysteine to tRNA(Cys) (PubMed:12662918). Unable to bind serine (PubMed:12662918). {ECO:0000269|PubMed:12662918}.; FUNCTION: In addition to its role as an aminoacyl-tRNA synthetase, has also cysteine persulfide synthase activity. Produces reactive persulfide species such as cysteine persulfide (CysSSH) from substrate cysteine and mediate direct incorporation of CysSSH into proteins during translations, resulting in protein persulfides and polysulfides (PubMed:29079736). CysSSHs behave as potent antioxidants and cellular protectants (PubMed:29079736). {ECO:0000269|PubMed:29079736}.

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.CYSTEINE--TRNA-LIGASE-RXN|reaction.ecocyc.CYSTEINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0526|gene.b0526]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21888`
- `KEGG:ecj:JW0515;eco:b0526;ecoc:C3026_02580;`
- `GeneID:946969;`
- `GO:GO:0004812; GO:0004817; GO:0005524; GO:0005737; GO:0005829; GO:0006423; GO:0008270; GO:0016874; GO:0046872`
- `EC:6.1.1.16`

## Notes

Cysteine--tRNA ligase (EC 6.1.1.16) (Cysteinyl-tRNA synthetase) (CysRS)
