---
entity_id: "gene.b3212"
entity_type: "gene"
name: "gltB"
source_database: "NCBI RefSeq"
source_id: "gene-b3212"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3212"
  - "gltB"
---

# gltB

`gene.b3212`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3212`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gltB (gene.b3212) is a gene entity. It encodes gltB (protein.P09831). Encoded protein function: FUNCTION: Catalyzes the conversion of L-glutamine and 2-oxoglutarate into two molecules of L-glutamate. {ECO:0000269|PubMed:4565085}. EcoCyc product frame: GLUSYNLARGE-MONOMER. EcoCyc synonyms: psiQ, ossB, aspB. Genomic coordinates: 3354725-3359185.

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0), fnr (protein.P0A9E5), crp (protein.P0ACJ8), nac (protein.Q47005). Activated by rpoD (protein.P00579), hdfR (protein.P0A8R9), lrp (protein.P0ACJ0), rpoS (protein.P13445), adiY (protein.P33234), gadE (protein.P63204).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09831|protein.P09831]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (11)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gltB; function=+
- `activates` <-- [[protein.P0A8R9|protein.P0A8R9]] `RegulonDB` `S` - regulator=HdfR; target=gltB; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=gltB; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=gltB; function=+
- `activates` <-- [[protein.P33234|protein.P33234]] `RegulonDB` `S` - regulator=AdiY; target=gltB; function=+
- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `C` - regulator=GadE; target=gltB; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=gltB; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=gltB; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=gltB; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=gltB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010545,ECOCYC:EG10403,GeneID:947724`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3354725-3359185:+; feature_type=gene
