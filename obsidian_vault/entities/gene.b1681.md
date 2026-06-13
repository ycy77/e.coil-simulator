---
entity_id: "gene.b1681"
entity_type: "gene"
name: "sufD"
source_database: "NCBI RefSeq"
source_id: "gene-b1681"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1681"
  - "sufD"
---

# sufD

`gene.b1681`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1681`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sufD (gene.b1681) is a gene entity. It encodes sufD (protein.P77689). Encoded protein function: FUNCTION: The SufBCD complex acts synergistically with SufE to stimulate the cysteine desulfurase activity of SufS. The SufBCD complex contributes to the assembly or repair of oxygen-labile iron-sulfur clusters under oxidative stress. May facilitate iron uptake from extracellular iron chelators under iron limitation. Required for the stability of the FhuF protein. {ECO:0000269|PubMed:10322040, ECO:0000269|PubMed:12941942}. EcoCyc product frame: G6907-MONOMER. EcoCyc synonyms: ynhC. Genomic coordinates: 1760520-1761791. EcoCyc protein note: The assembly of iron-sulfur clusters requires complex biosynthetic machinery. E. coli encodes two sets of proteins, the Isc and the Suf system, to achieve this task. SufD is a component of the SufBC2D Fe-S cluster assembly scaffold complex. Both SufC and SufD are required for Fe-S cluster formation on SufB in vivo. The SufD subunit is dispensible for sulfur transfer in vivo, but it is required for the acquisition of iron . The Cys405 residue of SufB and the His360 residue of SufD, located next to each other at the SufB-SufD interface, are required for Fe-S cluster assembly . A crystal structure of the SufC2-SufD2 complex has been determined at 2.2 Å resolution...

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by rpoD (protein.P00579), oxyR (protein.P0ACQ4), iscR (protein.P0AGK8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77689|protein.P77689]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sufD; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=sufD; function=+
- `activates` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=sufD; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=sufD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005617,ECOCYC:G6907,GeneID:944878`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1760520-1761791:-; feature_type=gene
