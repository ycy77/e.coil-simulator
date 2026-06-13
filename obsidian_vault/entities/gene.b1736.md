---
entity_id: "gene.b1736"
entity_type: "gene"
name: "chbA"
source_database: "NCBI RefSeq"
source_id: "gene-b1736"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1736"
  - "chbA"
---

# chbA

`gene.b1736`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1736`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

chbA (gene.b1736) is a gene entity. It encodes chbA (protein.P69791). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II ChbABC PTS system is involved in the transport of the chitin disaccharide N,N'-diacetylchitobiose (GlcNAc2) (PubMed:10913117, PubMed:10913118). Also able to use N,N',N''-triacetyl chitotriose (GlcNAc3) (PubMed:10913117). {ECO:0000269|PubMed:10913117, ECO:0000269|PubMed:10913118, ECO:0000305|PubMed:2092358}. EcoCyc product frame: CELC-MONOMER. EcoCyc synonyms: celC. Genomic coordinates: 1819455-1819805. EcoCyc protein note: ChbA contains a PTS Enzyme IIA domain. IIAchb has been shown to form stable homodimers , though the solution structure of a mutant IIAChb determined by NMR spectroscopy suggests that a homotrimer is the primary oligomeric state of IIAchb. The active site histidine (His89) is located within a crevice formed at the interface of two adjacent subunits of the EIIAChb trimer . A solution structure of a ChbA-ChbB complex has been obtained and the interaction sites mapped...

## Biological Role

Repressed by nagC (protein.P0AF20), chbR (protein.P17410). Activated by crp (protein.P0ACJ8), chbR (protein.P17410).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69791|protein.P69791]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=chbA; function=+
- `activates` <-- [[protein.P17410|protein.P17410]] `RegulonDB` `S` - regulator=ChbR; target=chbA; function=-+
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `S` - regulator=NagC; target=chbA; function=-
- `represses` <-- [[protein.P17410|protein.P17410]] `RegulonDB` `S` - regulator=ChbR; target=chbA; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0005792,ECOCYC:EG10142,GeneID:946244`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1819455-1819805:-; feature_type=gene
