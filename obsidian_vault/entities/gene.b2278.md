---
entity_id: "gene.b2278"
entity_type: "gene"
name: "nuoL"
source_database: "NCBI RefSeq"
source_id: "gene-b2278"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2278"
  - "nuoL"
---

# nuoL

`gene.b2278`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2278`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nuoL (gene.b2278) is a gene entity. It encodes nuoL (protein.P33607). Encoded protein function: FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. EcoCyc product frame: NUOL-MONOMER. Genomic coordinates: 2393205-2395046. EcoCyc protein note: NuoL is part of the inner membrane component of NADH dehydrogenase I . The protein has 14 transmembrane helices and a 110 Å long amphipathic α-helix that spans almost the entire length of the membrane domain . Transmembrane helices were assigned to locations in the crystal structure using Fourier transform analysis . A crystal structure of the membrane component at higher resolution has allowed better identification of the unusual arrangement of the transmembrane helices . NuoL was proposed to be located at the distal end of the membrane arm of NDH-1 and to function in proton translocation...

## Biological Role

Repressed by ryhB (gene.b4451), fnr (protein.P0A9E5), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33607|protein.P33607]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nuoL; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nuoL; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=nuoL; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=nuoL; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=nuoL; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=nuoL; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007532,ECOCYC:EG12092,GeneID:945540`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2393205-2395046:-; feature_type=gene
