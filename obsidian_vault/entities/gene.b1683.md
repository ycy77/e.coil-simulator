---
entity_id: "gene.b1683"
entity_type: "gene"
name: "sufB"
source_database: "NCBI RefSeq"
source_id: "gene-b1683"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1683"
  - "sufB"
---

# sufB

`gene.b1683`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1683`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sufB (gene.b1683) is a gene entity. It encodes sufB (protein.P77522). Encoded protein function: FUNCTION: The SufBCD complex acts synergistically with SufE to stimulate the cysteine desulfurase activity of SufS. The SufBCD complex contributes to the assembly or repair of oxygen-labile iron-sulfur clusters under oxidative stress. May facilitate iron uptake from extracellular iron chelators under iron limitation. {ECO:0000269|PubMed:12941942, ECO:0000269|PubMed:19810706}. EcoCyc product frame: G6909-MONOMER. EcoCyc synonyms: ynhE. Genomic coordinates: 1762522-1764009. EcoCyc protein note: The assembly of iron-sulfur clusters requires complex biosynthetic machinery. E. coli encodes two sets of proteins, the Isc and the Suf system, to achieve this task. The SufE protein transfers sulfur to SufB , which is a component of the SufBC2D Fe-S cluster assembly scaffold complex. The SufBCD complex activates the cysteine desulfurase activity of SufSE, likely by acting as the sulfur acceptor . The Cys405 residue of SufB and the His360 residue of SufD, located next to each other at the SufB-SufD interface, are required for Fe-S cluster assembly . The Cys254 residue of SufB is required for transfer of sulfur from SufE...

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by rpoD (protein.P00579), oxyR (protein.P0ACQ4), iscR (protein.P0AGK8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77522|protein.P77522]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sufB; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=sufB; function=+
- `activates` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `C` - regulator=IscR; target=sufB; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=sufB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005621,ECOCYC:G6909,GeneID:945753`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1762522-1764009:-; feature_type=gene
