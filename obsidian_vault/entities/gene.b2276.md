---
entity_id: "gene.b2276"
entity_type: "gene"
name: "nuoN"
source_database: "NCBI RefSeq"
source_id: "gene-b2276"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2276"
  - "nuoN"
---

# nuoN

`gene.b2276`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2276`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nuoN (gene.b2276) is a gene entity. It encodes nuoN (protein.P0AFF0). Encoded protein function: FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. EcoCyc product frame: NUON-MONOMER. Genomic coordinates: 2390048-2391505. EcoCyc protein note: NuoN is part of the inner membrane component of NADH dehydrogenase I . The protein has 14 transmembrane helices . The transmembrane topology of NuoN has been investigated, supporting data from the crystal structure and indicating that both the N and C terminus are located in the periplasm . Transmembrane helices were assigned to locations in the crystal structure using Fourier transform analysis . A crystal structure of the membrane component at higher resolution has allowed better identification of the unusual arrangement of the transmembrane helices . This subunit may function in proton translocation . Site-directed mutagenesis has identified residues important for dNADH oxidase activity, proton translocation, and interaction with quinones...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), ryhB (gene.b4451), fnr (protein.P0A9E5), arcA (protein.P0A9Q1), ompR (protein.P0AA16). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFF0|protein.P0AFF0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nuoN; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nuoN; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=nuoN; function=+
- `represses` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=nuoN; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=nuoN; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=nuoN; function=-
- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=nuoN; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007526,ECOCYC:EG12093,GeneID:945136`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2390048-2391505:-; feature_type=gene
