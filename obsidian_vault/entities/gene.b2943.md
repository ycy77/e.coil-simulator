---
entity_id: "gene.b2943"
entity_type: "gene"
name: "galP"
source_database: "NCBI RefSeq"
source_id: "gene-b2943"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2943"
  - "galP"
---

# galP

`gene.b2943`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2943`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

galP (gene.b2943) is a gene entity. It encodes galP (protein.P0AEP1). Encoded protein function: FUNCTION: Uptake of galactose across the boundary membrane with the concomitant transport of protons into the cell (symport system). EcoCyc product frame: GALP-MONOMER. EcoCyc synonyms: Pgal. Genomic coordinates: 3088284-3089678. EcoCyc protein note: GalP is a member of the Major Facilitator Superfamily (MFS) of transporters and is one of two, along with MglABC, major routes for galactose transport into E. coli K-12. 2-deoxy-D-galactose is a specific substrate for GalP but not for MglABC and GalP operates by a sugar-proton symport mechanism while MglABC does not . Mutation studies demonstrated that insertions in the galP gene resulted in a mutant strain resistant to 2-deoxygalactose and defective in uptake of radiolabelled 2-deoxyglucose. The GalP protein has been overproduced and purified and reconstituted as a galactose transporter and has been shown to share a high level of sequence similarity with other proton-linked systems for L-arabinose (AraE, 64% identity) and for D-xylose (XylE, 34% identity) in E.coli . Equilibrium binding studies indicate that cytochalasin B, which is a potent inhibitor of passive glucose transporters in mammals, is bound with high-affinity by membranes of an E. coli strain constitutive for GalP...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), galR (protein.P03024), ompR (protein.P0AA16), nagC (protein.P0AF20), galS (protein.P25748). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEP1|protein.P0AEP1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=galP; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P03024|protein.P03024]] `RegulonDB` `C` - regulator=GalR; target=galP; function=-
- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=galP; function=-
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=galP; function=-
- `represses` <-- [[protein.P25748|protein.P25748]] `RegulonDB` `C` - regulator=GalS; target=galP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009654,ECOCYC:EG12148,GeneID:947434`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3088284-3089678:+; feature_type=gene
