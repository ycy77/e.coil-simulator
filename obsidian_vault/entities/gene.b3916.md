---
entity_id: "gene.b3916"
entity_type: "gene"
name: "pfkA"
source_database: "NCBI RefSeq"
source_id: "gene-b3916"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3916"
  - "pfkA"
---

# pfkA

`gene.b3916`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3916`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pfkA (gene.b3916) is a gene entity. It encodes pfkA (protein.P0A796). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of D-fructose 6-phosphate to fructose 1,6-bisphosphate by ATP, the first committing step of glycolysis (PubMed:2953977, PubMed:3158524). In addition, is involved in the utilization of D-sedoheptulose 7-phosphate, an intermediate of the pentose phosphate pathway, via the sedoheptulose bisphosphate bypass pathway (PubMed:19756045). Catalyzes the phosphorylation of D-sedoheptulose 7-phosphate to D-sedoheptulose 1,7-bisphosphate (PubMed:19756045). {ECO:0000269|PubMed:19756045, ECO:0000269|PubMed:2953977, ECO:0000269|PubMed:3158524}. EcoCyc product frame: 6PFK-1-MONOMER. Genomic coordinates: 4107552-4108514.

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by FlhDC DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-3930), rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco03018` RNA degradation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A796|protein.P0A796]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-3930|complex.ecocyc.CPLX0-3930]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pfkA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=pfkA; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=pfkA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012789,ECOCYC:EG10699,GeneID:948412`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4107552-4108514:+; feature_type=gene
