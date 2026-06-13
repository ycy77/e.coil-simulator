---
entity_id: "gene.b3829"
entity_type: "gene"
name: "metE"
source_database: "NCBI RefSeq"
source_id: "gene-b3829"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3829"
  - "metE"
---

# metE

`gene.b3829`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3829`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metE (gene.b3829) is a gene entity. It encodes metE (protein.P25665). Encoded protein function: FUNCTION: Catalyzes the transfer of a methyl group from 5-methyltetrahydrofolate to homocysteine resulting in methionine formation. {ECO:0000255|HAMAP-Rule:MF_00172}. EcoCyc product frame: HOMOCYSMET-MONOMER. EcoCyc synonyms: metB12. Genomic coordinates: 4013053-4015314. EcoCyc protein note: In the absence of exogenously supplied vitamin B12 (cobalamin), E. coli MetE catalyzes the final step of de novo methionine biosynthesis. In the presence of the vitamin B12 cofactor, MetH functions in this reaction and synthesis of MetE is repressed (see pathway HOMOSER-METSYN-PWY). The metE and metH genes lack similarity in their deduced amino acid sequences, suggesting that these proteins arose by convergent evolution . MetE was shown to utilize only the triglutamate form of folate (5-methyltetrahydropteroyltri-L-glutamate) whereas MetH utilized either the monoglutamate (5-methyl-tetrahydrofolate) or the triglutamate forms of folate . Early studies utilized unpurified or partially purified enzyme . The enzyme was later purified from extracts of E. coli K-12 and characterized . The metE gene was cloned and expressed and the expression of MetE was shown to be repressed by methionine and vitamin B12 . Recombinant enzyme has also been purified and characterized...

## Biological Role

Repressed by metJ (protein.P0A8U6). Activated by DNA-binding transcriptional dual regulator Cra (complex.ecocyc.PC00061), metR (protein.P0A9F9), oxyR (protein.P0ACQ4), nac (protein.Q47005).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25665|protein.P25665]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[complex.ecocyc.PC00061|complex.ecocyc.PC00061]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9F9|protein.P0A9F9]] `RegulonDB` `S` - regulator=MetR; target=metE; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=metE; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=metE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A8U6|protein.P0A8U6]] `RegulonDB` `S` - regulator=MetJ; target=metE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012520,ECOCYC:EG10584,GeneID:948323`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4013053-4015314:+; feature_type=gene
