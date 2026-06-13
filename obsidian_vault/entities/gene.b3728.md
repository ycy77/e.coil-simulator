---
entity_id: "gene.b3728"
entity_type: "gene"
name: "pstS"
source_database: "NCBI RefSeq"
source_id: "gene-b3728"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3728"
  - "pstS"
---

# pstS

`gene.b3728`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3728`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pstS (gene.b3728) is a gene entity. It encodes pstS (protein.P0AG82). Encoded protein function: FUNCTION: Part of the ABC transporter complex PstSACB involved in phosphate import. EcoCyc product frame: PSTS-MONOMER. EcoCyc synonyms: R2pho, T, nmpA, phoR2a, phoS. Genomic coordinates: 3910485-3911525. EcoCyc protein note: PstS is the periplasmic, phosphate binding protein of the ATP dependent, high affinity phosphate transport sytem in E. coli K-12. PstS consists of two globular domains separated by a deep cleft which forms the phosphate binding site . PstS binds monobasic (H2PO4-) and dibasic (H2PO42-) phosphates but discriminates against sulphate . The aspartate residue at position 81 forms a short (low barrier) hydrogen bond with phosphate . PstS can discriminate phosphate from arsenate up to an 800 fold molar excess of arsenate . A pstS D81N mutant has no effect on phosphate binding but disturbs the discrimination against arsenate approximately 10-fold and the discrimination against sulfate about 100-fold . pstS insertion mutants were identified in a screen for genes that are important for surviving exposure to ionizing radiation (IR). A pstS deletion mutant has a substantial decrease in survival upon exposure to increasing doses of IR . It was determined by Genomic SELEX screening that the upstream region of the gene pstS is a target of the transcriptional factor CusR .

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5), rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG82|protein.P0AG82]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pstS; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=pstS; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=pstS; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=pstS; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012190,ECOCYC:EG10734,GeneID:948237`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3910485-3911525:-; feature_type=gene
