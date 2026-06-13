---
entity_id: "gene.b1738"
entity_type: "gene"
name: "chbB"
source_database: "NCBI RefSeq"
source_id: "gene-b1738"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1738"
  - "chbB"
---

# chbB

`gene.b1738`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1738`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

chbB (gene.b1738) is a gene entity. It encodes chbB (protein.P69795). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II ChbABC PTS system is involved in the transport of the chitin disaccharide N,N'-diacetylchitobiose (GlcNAc2) (PubMed:10913117). Also able to use N,N',N''-triacetyl chitotriose (GlcNAc3) (PubMed:10913117, PubMed:10913119). {ECO:0000269|PubMed:10913117, ECO:0000269|PubMed:10913119, ECO:0000305|PubMed:2092358}. EcoCyc product frame: CELA-MONOMER. EcoCyc synonyms: celA. Genomic coordinates: 1821299-1821619. EcoCyc protein note: ChbB contains a PTS Enzyme IIB domain. Cys10 is the site of phosphotransfer during the PTScbh reaction sequence . The 3-dimensional structure of IIBChb has been determined by NMR spectroscopy and by X-ray crystallography to a resolution of 1.8 Å . A solution structure of a ChbB-ChbA complex has been obtained and the interaction sites mapped. The protruding active site of ChbB containing the active site cysteine residue (Cys10) is buried within the cleft formed by the adjacent subunits of the ChbA trimer . chbB: N,N'-diacetylchitobiose B

## Biological Role

Repressed by nagC (protein.P0AF20), chbR (protein.P17410). Activated by crp (protein.P0ACJ8), chbR (protein.P17410).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69795|protein.P69795]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=chbB; function=+
- `activates` <-- [[protein.P17410|protein.P17410]] `RegulonDB` `S` - regulator=ChbR; target=chbB; function=-+
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `S` - regulator=NagC; target=chbB; function=-
- `represses` <-- [[protein.P17410|protein.P17410]] `RegulonDB` `S` - regulator=ChbR; target=chbB; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0005797,ECOCYC:EG10140,GeneID:945339`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1821299-1821619:-; feature_type=gene
