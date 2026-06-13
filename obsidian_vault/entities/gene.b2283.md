---
entity_id: "gene.b2283"
entity_type: "gene"
name: "nuoG"
source_database: "NCBI RefSeq"
source_id: "gene-b2283"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2283"
  - "nuoG"
---

# nuoG

`gene.b2283`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2283`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nuoG (gene.b2283) is a gene entity. It encodes nuoG (protein.P33602). Encoded protein function: FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. EcoCyc product frame: NUOG-MONOMER. Genomic coordinates: 2397439-2400165. EcoCyc protein note: NuoG is part of the soluble fragment of NADH dehydrogenase I, which represents the electron input part of the enzyme . NuoG is essential for NDH-1 function . This subunit contains the 2Fe-2S cluster N1b and three 4Fe-4S clusters. N7 was formerly misidentified as "N1c", whose EPR signal is in fact derived from the 2Fe-2S cluster N1a on the NuoE subunit . N7 is non-conserved and not thought to be involved in electron transfer; however, it is essential for the stability of NDH-1 . The cysteine residues responsible for ligation of the 4Fe-4S clusters were identified by site-directed mutagenesis . However, the location and identity of EPR spectra for the N4 and N5 Fe-S clusters were subject of some controversy...

## Biological Role

Repressed by ryhB (gene.b4451), fnr (protein.P0A9E5), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33602|protein.P33602]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nuoG; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nuoG; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=nuoG; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=nuoG; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=nuoG; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=nuoG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007543,ECOCYC:EG12087,GeneID:946762`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2397439-2400165:-; feature_type=gene
