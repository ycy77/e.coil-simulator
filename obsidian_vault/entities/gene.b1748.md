---
entity_id: "gene.b1748"
entity_type: "gene"
name: "astC"
source_database: "NCBI RefSeq"
source_id: "gene-b1748"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1748"
  - "astC"
---

# astC

`gene.b1748`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1748`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

astC (gene.b1748) is a gene entity. It encodes astC (protein.P77581). Encoded protein function: FUNCTION: Catalyzes the transamination of N(2)-succinylornithine and alpha-ketoglutarate into N(2)-succinylglutamate semialdehyde and glutamate. Can also act as an acetylornithine aminotransferase. Is involved in the utilization of arginine as a nitrogen source, via the AST pathway, and also seems to play a role in ornithine catabolism (PubMed:9696779). {ECO:0000269|PubMed:9696779}. EcoCyc product frame: SUCCORNTRANSAM-MONOMER. EcoCyc synonyms: ydjW, argM, cstC. Genomic coordinates: 1830762-1831982. EcoCyc protein note: Succinylornithine transaminase (AstC) catalyzes the third reaction in the ammonia-producing arginine catabolic pathway, AST-PWY. The astC gene is 60% identical to EG10066 "argD", which encodes the arginine-repressible N-acetylornithine aminotransferase . Four enzymes, ArgD, AstC, GabT, and PuuE, show some level of N-acetylornithine aminotransferase (ACOAT) activity involved in arginine biosynthesis. On minimal medium lacking arginine, single argD or astC mutants have subtle growth defects, and an argD astC double mutant has a slower doubling time than wild type. An argD astC gabT triple mutant does not grow on medium lacking arginine...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), rob (protein.P0ACI0), lrp (protein.P0ACJ0). Activated by argR (protein.P0A6D0), lrp (protein.P0ACJ0), glnG (protein.P0AFB8), rpoS (protein.P13445), rpoN (protein.P24255).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77581|protein.P77581]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=astC; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=astC; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=astC; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `C` - sigma=sigma54; target=astC; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACI0|protein.P0ACI0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005824,ECOCYC:G6944,GeneID:946255`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1830762-1831982:-; feature_type=gene
