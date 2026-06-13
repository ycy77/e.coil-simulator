---
entity_id: "gene.b2697"
entity_type: "gene"
name: "alaS"
source_database: "NCBI RefSeq"
source_id: "gene-b2697"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2697"
  - "alaS"
---

# alaS

`gene.b2697`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2697`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alaS (gene.b2697) is a gene entity. It encodes alaS (protein.P00957). Encoded protein function: FUNCTION: Catalyzes the attachment of L-alanine to tRNA(Ala) in a two-step reaction: L-alanine is first activated by ATP to form Ala-AMP and then transferred to the acceptor end of tRNA(Ala) (PubMed:28362257). AlaRS also incorrectly activates the sterically smaller amino acid glycine as well as the sterically larger amino acid L-serine; generates 2-fold more mischarged Gly than Ser (PubMed:28362257). These mischarged amino acids occur because the of inherent physicochemical limitations on discrimination between closely related amino acids (Ala, Gly and Ser) in the charging step (PubMed:28362257). In presence of high levels of lactate, also acts as a protein lactyltransferase that mediates lactylation of lysine residues in target proteins (PubMed:38653238, PubMed:39322678). {ECO:0000269|PubMed:28362257, ECO:0000269|PubMed:38653238, ECO:0000269|PubMed:39322678}.; FUNCTION: Edits mischarged Ser-tRNA(Ala) and Gly-tRNA(Ala) but not incorrectly charged Ser-tRNA(Thr) (PubMed:12554667, PubMed:18723508). Dtd edits Gly-tRNA(Ala) 4-fold better than does AlaRS (PubMed:28362257). {ECO:0000269|PubMed:12554667, ECO:0000269|PubMed:18723508, ECO:0000269|PubMed:28362257}.; FUNCTION: Attaches Ala to transfer-messenger RNA (tmRNA, also known as 10Sa RNA, the product of the ssrA gene)...

## Biological Role

Repressed by alaS (protein.P00957), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00957|protein.P00957]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P00957|protein.P00957]] `RegulonDB` `C` - regulator=AlaS; target=alaS; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008869,ECOCYC:EG10034,GeneID:947175`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2819381-2822011:-; feature_type=gene
