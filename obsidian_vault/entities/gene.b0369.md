---
entity_id: "gene.b0369"
entity_type: "gene"
name: "hemB"
source_database: "NCBI RefSeq"
source_id: "gene-b0369"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0369"
  - "hemB"
---

# hemB

`gene.b0369`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0369`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hemB (gene.b0369) is a gene entity. It encodes hemB (protein.P0ACB2). Encoded protein function: FUNCTION: Catalyzes an early step in the biosynthesis of tetrapyrroles. Binds two molecules of 5-aminolevulinate per subunit, each at a distinct site, and catalyzes their condensation to form porphobilinogen. EcoCyc product frame: PORPHOBILSYNTH-MONOMER. EcoCyc synonyms: ncf. Genomic coordinates: 388753-389727. EcoCyc protein note: Porphobilinogen synthase (HemB) catalyzes the synthesis of porphobilinogen by an asymmetric condensation of two molecules of 5-aminolevulinate (ALA) via a Schiff-base intermediate . suggested that HemB may be feedback-inhibited by protoporphyrinogen IX, an intermediate in the PWY0-1415 heme biosynthesis pathway. HemB is a metalloenzyme that requires Zn2+ for activity . Mg2+ is not required for activity, however, addition results in stimulation of activity . Two distinct metal binding sites have been identified and characterized and correlated with two ALA binding sites . The asymmetry of the condensation reaction is supported by the two unequal ALA binding sites. Binding of ALA to HemB is ordered, binding at the P-site first; structural requirements for substrate binding to the A- and P-sites differ . The Km for each of the two ALA binding sites has been measured...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACB2|protein.P0ACB2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=hemB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001266,ECOCYC:EG10428,GeneID:945017`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:388753-389727:-; feature_type=gene
