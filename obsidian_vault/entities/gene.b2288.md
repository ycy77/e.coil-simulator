---
entity_id: "gene.b2288"
entity_type: "gene"
name: "nuoA"
source_database: "NCBI RefSeq"
source_id: "gene-b2288"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2288"
  - "nuoA"
---

# nuoA

`gene.b2288`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2288`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nuoA (gene.b2288) is a gene entity. It encodes nuoA (protein.P0AFC3). Encoded protein function: FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. EcoCyc product frame: NUOA-MONOMER. Genomic coordinates: 2404629-2405072. EcoCyc protein note: NuoA is part of the inner membrane component of NADH dehydrogenase I . The protein has three predicted transmembrane domains , and the C terminus is located in the cytoplasm . Site-specific mutagenesis of conserved charged amino acid residues has elucidated possible functional roles for Asp79 and Glu81 . A crystal structure of the membrane component at higher resolution has allowed better identification of the interactions between the subunits . In the presence of NADH, crosslinking between NuoA and NuoJ in the intact Complex I is abolished, indicating that the conformational change involving the hydrophilic subunits in the presence of NADH extends to the membrane domain...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), ryhB (gene.b4451), fnr (protein.P0A9E5), arcA (protein.P0A9Q1), lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFC3|protein.P0AFC3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nuoA; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nuoA; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=nuoA; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=nuoA; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=nuoA; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=nuoA; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007553,ECOCYC:EG12082,GeneID:946764`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2404629-2405072:-; feature_type=gene
