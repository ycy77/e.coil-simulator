---
entity_id: "gene.b2282"
entity_type: "gene"
name: "nuoH"
source_database: "NCBI RefSeq"
source_id: "gene-b2282"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2282"
  - "nuoH"
---

# nuoH

`gene.b2282`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2282`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nuoH (gene.b2282) is a gene entity. It encodes nuoH (protein.P0AFD4). Encoded protein function: FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. This subunit may bind ubiquinone. EcoCyc product frame: NUOH-MONOMER. Genomic coordinates: 2396465-2397442. EcoCyc protein note: NuoH is part of the inner membrane component of NADH dehydrogenase I . The protein has eight predicted transmembrane domains; the C terminus is located in the periplasm . This subunit was thought to contain the ubiquinone binding site , which has since been proposed to be located in the NuoM subunit . However, an E36Q mutant shows higher apparent Km for ubiquinone, suggesting proximity to the ubiquinone binding domain . The charged residues of the cytoplasmic loops are highly conserved; mutagenesis of these residues results in loss of enzymatic activity and a low content of the peripheral subunits NuoB and NuoCD, indicating that the cytoplasmic loops are essential for assembly of the peripheral arm of NDH-1...

## Biological Role

Repressed by ryhB (gene.b4451), fnr (protein.P0A9E5), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFD4|protein.P0AFD4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nuoH; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nuoH; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=nuoH; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=nuoH; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=nuoH; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=nuoH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007541,ECOCYC:EG12088,GeneID:946761`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2396465-2397442:-; feature_type=gene
