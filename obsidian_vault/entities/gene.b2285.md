---
entity_id: "gene.b2285"
entity_type: "gene"
name: "nuoE"
source_database: "NCBI RefSeq"
source_id: "gene-b2285"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2285"
  - "nuoE"
---

# nuoE

`gene.b2285`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2285`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nuoE (gene.b2285) is a gene entity. It encodes nuoE (protein.P0AFD1). Encoded protein function: FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. EcoCyc product frame: NUOE-MONOMER. Genomic coordinates: 2401552-2402052. EcoCyc protein note: NuoE is part of the soluble fragment of NADH dehydrogenase I (NDH-1), which represents the electron input part of the enzyme . Based on sequence similarity, this subunit is predicted to contain the N1a 2Fe-2S cluster . The location of the conserved N1a cluster suggests that it does not participate in electron transfer chain through NDH-1. Site-directed mutagenesis of the cysteine residues expected to coordinate the N1a cluster resulted in the loss of N1a and significantly reduced the amount of the N1b cluster coordinated by the NuoG subunit. Only the C97A mutant retained most of the N1a cluster. The mutants showed reduced NHD-1 activity, but severely affected the stability of the NDH-1 complex...

## Biological Role

Repressed by ryhB (gene.b4451), fnr (protein.P0A9E5), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFD1|protein.P0AFD1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nuoE; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nuoE; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=nuoE; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=nuoE; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=nuoE; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=nuoE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007547,ECOCYC:EG12086,GeneID:946746`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2401552-2402052:-; feature_type=gene
