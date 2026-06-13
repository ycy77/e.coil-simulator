---
entity_id: "gene.b0222"
entity_type: "gene"
name: "gmhA"
source_database: "NCBI RefSeq"
source_id: "gene-b0222"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0222"
  - "gmhA"
---

# gmhA

`gene.b0222`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0222`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gmhA (gene.b0222) is a gene entity. It encodes gmhA (protein.P63224). Encoded protein function: FUNCTION: Catalyzes the isomerization of sedoheptulose 7-phosphate in D-glycero-D-manno-heptose 7-phosphate. {ECO:0000269|PubMed:11751812, ECO:0000269|PubMed:18056714}. EcoCyc product frame: G6106-MONOMER. EcoCyc synonyms: yafI, lpcA, tfrA. Genomic coordinates: 243543-244121. EcoCyc protein note: Sedoheptulose 7-phosphate isomerase catalyzes the first committed step in the biosynthesis of a core component of lipopolysaccharide, the isomerization of D-sedoheptulose 7-phosphate to D-glycero-D-manno-heptose 7-phosphate. Crystal structures of GmhA alone and in complex with the substrate D-sedoheptulose 7-phosphate have been solved. The protein appears to be a tetramer in both the crystal structures and in solution. A reaction mechanism utilizing an enediol intermediate has been proposed . Potential active site residues were mutagenized and their enzymatic activity was measured both in vivo and in vitro . Mutations in gmhA confer novobiocin hypersensitivity and F plasmid conjugation deficiency ; gmhA mutants were shown to contain lipopolysaccharides lacking heptose . An IS1 insertion in the Shine-Dalgarno sequence of gmhA was isolated as a suppressor of a ΔlapB mutant...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748). Activated by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), ompR (protein.P0AA16), pdhR (protein.P0ACL9).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P63224|protein.P63224]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=gmhA; function=+
- `activates` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=gmhA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000751,ECOCYC:G6106,GeneID:949134`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:243543-244121:+; feature_type=gene
