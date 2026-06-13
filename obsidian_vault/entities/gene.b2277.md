---
entity_id: "gene.b2277"
entity_type: "gene"
name: "nuoM"
source_database: "NCBI RefSeq"
source_id: "gene-b2277"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2277"
  - "nuoM"
---

# nuoM

`gene.b2277`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2277`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nuoM (gene.b2277) is a gene entity. It encodes nuoM (protein.P0AFE8). Encoded protein function: FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. EcoCyc product frame: NUOM-MONOMER. EcoCyc synonyms: nuoA. Genomic coordinates: 2391512-2393041. EcoCyc protein note: NuoM is part of the inner membrane component of NADH dehydrogenase I . The protein has 14 transmembrane helices . Transmembrane helices were assigned to locations in the crystal structure using Fourier transform analysis . A crystal structure of the membrane component at higher resolution has allowed better identification of the unusual arrangement of the transmembrane helices . This subunit may function in proton translocation and may contain the ubiquinone binding site . Site-directed mutagenesis of various conserved amino acid residues suggest that E144 and K234 are essential for energy transduction and may thus participate in proton translocation...

## Biological Role

Repressed by ryhB (gene.b4451), fnr (protein.P0A9E5), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFE8|protein.P0AFE8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nuoM; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nuoM; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=nuoM; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=nuoM; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=nuoM; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=nuoM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007529,ECOCYC:EG11773,GeneID:947731`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2391512-2393041:-; feature_type=gene
