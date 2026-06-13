---
entity_id: "gene.b2287"
entity_type: "gene"
name: "nuoB"
source_database: "NCBI RefSeq"
source_id: "gene-b2287"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2287"
  - "nuoB"
---

# nuoB

`gene.b2287`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2287`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nuoB (gene.b2287) is a gene entity. It encodes nuoB (protein.P0AFC7). Encoded protein function: FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. EcoCyc product frame: NUOB-MONOMER. Genomic coordinates: 2403951-2404613. EcoCyc protein note: NuoB is part of the connecting fragment of NADH dehydrogenase I . This subunit contains the N2 4Fe-4S cluster , which may play a role in proton translocation activity of NDH I . The Glu67 residue is most likely protonated by oxidation of the N2 cluster, and is involved in proton translocation . A mechanism by which the redox reaction at the N2 cluster induces conformational changes leading to proton translocation has been proposed . Point mutations in NuoB have been analyzed; the Tyr114 and Tyr139 residues appear to be protonated upon reduction of the 4Fe-4S cluster, and a double mutant retains only 20% activity . Mutagenesis of the conserved acidic residues E67, D77, and D94 abolishes electron transfer activity of NDH I...

## Biological Role

Repressed by ryhB (gene.b4451), fnr (protein.P0A9E5), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFC7|protein.P0AFC7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nuoB; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nuoB; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=nuoB; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=nuoB; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=nuoB; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=nuoB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007551,ECOCYC:EG12083,GeneID:946738`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2403951-2404613:-; feature_type=gene
