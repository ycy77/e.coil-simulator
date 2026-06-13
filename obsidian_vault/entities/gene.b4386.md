---
entity_id: "gene.b4386"
entity_type: "gene"
name: "lplA"
source_database: "NCBI RefSeq"
source_id: "gene-b4386"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4386"
  - "lplA"
---

# lplA

`gene.b4386`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4386`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lplA (gene.b4386) is a gene entity. It encodes lplA (protein.P32099). Encoded protein function: FUNCTION: Catalyzes both the ATP-dependent activation of exogenously supplied lipoate to lipoyl-AMP and the transfer of the activated lipoyl onto the lipoyl domains of lipoate-dependent enzymes. Is also able to catalyze very poorly the transfer of lipoyl and octanoyl moiety from their acyl carrier protein. {ECO:0000269|PubMed:7639702}. EcoCyc product frame: EG11796-MONOMER. EcoCyc synonyms: yjjF, slr. Genomic coordinates: 4623101-4624117. EcoCyc protein note: LplA is a lipoyl-protein ligase . Lipoate modification of the E2 subunits is important for the function of PYRUVATEDEH-CPLX , 2OXOGLUTARATEDEH-CPLX "α-ketoglutarate dehydrogenase" , and the GCVMULTI-CPLX . It was initially thought that LplA only utilizes lipoate imported from outside the cell, in contrast to the other lipoyl-protein ligase, LipB, which utilizes octanoyl-ACP. However, E. coli lipB mutants are able to grow with externally supplied octanoate instead of lipoate. Octanoate growth requires both LplA and CPLX0-782, the enzyme that converts octanoyl side chains to lipoyl side chains, suggesting that LplA attaches octanoate to the E2 domain, and CPLX0-782 converts the octanoate to lipoate . The two-part reaction requires ATP and Mg2+ and proceeds through a lipoyl-AMP intermediate...

## Enriched Pathways

- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32099|protein.P32099]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014385,ECOCYC:EG11796,GeneID:944865`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4623101-4624117:-; feature_type=gene
