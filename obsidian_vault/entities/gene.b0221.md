---
entity_id: "gene.b0221"
entity_type: "gene"
name: "fadE"
source_database: "NCBI RefSeq"
source_id: "gene-b0221"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0221"
  - "fadE"
---

# fadE

`gene.b0221`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0221`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fadE (gene.b0221) is a gene entity. It encodes fadE (protein.Q47146). Encoded protein function: FUNCTION: Catalyzes the dehydrogenation of acyl-coenzymes A (acyl-CoAs) to 2-enoyl-CoAs, the first step of the beta-oxidation cycle of fatty acid degradation. Is required for E.coli to utilize dodecanoate or oleate as the sole carbon and energy source for growth. {ECO:0000269|PubMed:12057976}. EcoCyc product frame: ACYLCOADEHYDROG-MONOMER. EcoCyc synonyms: yafH. Genomic coordinates: 240859-243303. EcoCyc protein note: Acyl-CoA dehydrogenase (FadE) catalyzes the first step in the degradation of fatty acids via the β-oxidation cycle . fadE mutants are unable to utilize oleate and other fatty acids as the sole source of carbon . The fadE62 allele is a single base deletion resulting in a frame shift mutation, and yafH can complement the phenotype of the fadE62 mutant strain . Expression of the enzymes involved in β-oxidation is normally induced by fatty acids of chain length 14 and longer . Regulation is at the transcriptional level and involves repression by FadR . OldE: "oleate degradation E"

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), fadR (protein.P0A8V6), arcA (protein.P0A9Q1). Activated by DNA-binding transcriptional dual regulator LldR-S-lactate (complex.ecocyc.CPLX0-7689), DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), ompR (protein.P0AA16), pdhR (protein.P0ACL9).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47146|protein.Q47146]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[complex.ecocyc.CPLX0-7689|complex.ecocyc.CPLX0-7689]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=fadE; function=+
- `activates` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=fadE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `S` - regulator=FadR; target=fadE; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `C` - regulator=ArcA; target=fadE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000743,ECOCYC:G6105,GeneID:949007`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:240859-243303:-; feature_type=gene
