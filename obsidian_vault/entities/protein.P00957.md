---
entity_id: "protein.P00957"
entity_type: "protein"
name: "alaS"
source_database: "UniProt"
source_id: "P00957"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "alaS lovB b2697 JW2667"
---

# alaS

`protein.P00957`

## Static

- Type: `protein`
- Source: `UniProt:P00957`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the attachment of L-alanine to tRNA(Ala) in a two-step reaction: L-alanine is first activated by ATP to form Ala-AMP and then transferred to the acceptor end of tRNA(Ala) (PubMed:28362257). AlaRS also incorrectly activates the sterically smaller amino acid glycine as well as the sterically larger amino acid L-serine; generates 2-fold more mischarged Gly than Ser (PubMed:28362257). These mischarged amino acids occur because the of inherent physicochemical limitations on discrimination between closely related amino acids (Ala, Gly and Ser) in the charging step (PubMed:28362257). In presence of high levels of lactate, also acts as a protein lactyltransferase that mediates lactylation of lysine residues in target proteins (PubMed:38653238, PubMed:39322678). {ECO:0000269|PubMed:28362257, ECO:0000269|PubMed:38653238, ECO:0000269|PubMed:39322678}.; FUNCTION: Edits mischarged Ser-tRNA(Ala) and Gly-tRNA(Ala) but not incorrectly charged Ser-tRNA(Thr) (PubMed:12554667, PubMed:18723508). Dtd edits Gly-tRNA(Ala) 4-fold better than does AlaRS (PubMed:28362257). {ECO:0000269|PubMed:12554667, ECO:0000269|PubMed:18723508, ECO:0000269|PubMed:28362257}.; FUNCTION: Attaches Ala to transfer-messenger RNA (tmRNA, also known as 10Sa RNA, the product of the ssrA gene). tmRNA plays a major role in rescue of stalled ribosomes via trans-translation. {ECO:0000269|PubMed:7524073}...

## Biological Role

Component of alanine—tRNA ligase/DNA-binding transcriptional repressor (complex.ecocyc.ALAS-CPLX), AlaS-L-alanine DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-7541).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

FUNCTION: Catalyzes the attachment of L-alanine to tRNA(Ala) in a two-step reaction: L-alanine is first activated by ATP to form Ala-AMP and then transferred to the acceptor end of tRNA(Ala) (PubMed:28362257). AlaRS also incorrectly activates the sterically smaller amino acid glycine as well as the sterically larger amino acid L-serine; generates 2-fold more mischarged Gly than Ser (PubMed:28362257). These mischarged amino acids occur because the of inherent physicochemical limitations on discrimination between closely related amino acids (Ala, Gly and Ser) in the charging step (PubMed:28362257). In presence of high levels of lactate, also acts as a protein lactyltransferase that mediates lactylation of lysine residues in target proteins (PubMed:38653238, PubMed:39322678). {ECO:0000269|PubMed:28362257, ECO:0000269|PubMed:38653238, ECO:0000269|PubMed:39322678}.; FUNCTION: Edits mischarged Ser-tRNA(Ala) and Gly-tRNA(Ala) but not incorrectly charged Ser-tRNA(Thr) (PubMed:12554667, PubMed:18723508). Dtd edits Gly-tRNA(Ala) 4-fold better than does AlaRS (PubMed:28362257). {ECO:0000269|PubMed:12554667, ECO:0000269|PubMed:18723508, ECO:0000269|PubMed:28362257}.; FUNCTION: Attaches Ala to transfer-messenger RNA (tmRNA, also known as 10Sa RNA, the product of the ssrA gene). tmRNA plays a major role in rescue of stalled ribosomes via trans-translation. {ECO:0000269|PubMed:7524073}.

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.ALAS-CPLX|complex.ecocyc.ALAS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7541|complex.ecocyc.CPLX0-7541]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b2697|gene.b2697]] `RegulonDB` `C` - regulator=AlaS; target=alaS; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2697|gene.b2697]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00957`
- `KEGG:ecj:JW2667;eco:b2697;ecoc:C3026_14845;`
- `GeneID:947175;`
- `GO:GO:0000049; GO:0001217; GO:0002161; GO:0002196; GO:0004813; GO:0005524; GO:0005829; GO:0006419; GO:0008270; GO:0016020; GO:0042802; GO:0042803; GO:0045892; GO:0141207`
- `EC:6.-.-.-; 6.1.1.7`

## Notes

Alanine--tRNA ligase (EC 6.1.1.7) (Alanyl-tRNA synthetase) (AlaRS) (Protein lactyltransferase) (EC 6.-.-.-)
