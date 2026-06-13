---
entity_id: "gene.b1737"
entity_type: "gene"
name: "chbC"
source_database: "NCBI RefSeq"
source_id: "gene-b1737"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1737"
  - "chbC"
---

# chbC

`gene.b1737`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1737`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

chbC (gene.b1737) is a gene entity. It encodes chbC (protein.P17334). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II ChbABC PTS system is involved in the transport of the chitin disaccharide N,N'-diacetylchitobiose (GlcNAc2) (PubMed:10913117). Also able to use N,N',N''-triacetyl chitotriose (GlcNAc3) (PubMed:10913117). {ECO:0000269|PubMed:10913117, ECO:0000305|PubMed:2092358}. EcoCyc product frame: CELB-MONOMER. EcoCyc synonyms: celB, hic. Genomic coordinates: 1819856-1821214. EcoCyc protein note: ChbC contains a PTS Enzyme IIC domain. ChbC is the integral membrane component of the chitobiose PTS and is predicted to contain the sugar binding site . chbC: N,N'-diacetylchitobiose C

## Biological Role

Repressed by nagC (protein.P0AF20), chbR (protein.P17410). Activated by crp (protein.P0ACJ8), chbR (protein.P17410).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17334|protein.P17334]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=chbC; function=+
- `activates` <-- [[protein.P17410|protein.P17410]] `RegulonDB` `S` - regulator=ChbR; target=chbC; function=-+
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=chbC; function=-
- `represses` <-- [[protein.P17410|protein.P17410]] `RegulonDB` `S` - regulator=ChbR; target=chbC; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0005795,ECOCYC:EG10141,GeneID:945982`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1819856-1821214:-; feature_type=gene
