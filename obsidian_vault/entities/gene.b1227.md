---
entity_id: "gene.b1227"
entity_type: "gene"
name: "narI"
source_database: "NCBI RefSeq"
source_id: "gene-b1227"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1227"
  - "narI"
---

# narI

`gene.b1227`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1227`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

narI (gene.b1227) is a gene entity. It encodes narI (protein.P11350). Encoded protein function: FUNCTION: The nitrate reductase enzyme complex allows E.coli to use nitrate as an electron acceptor during anaerobic growth. The gamma chain is a membrane-embedded heme-iron unit resembling cytochrome b, which transfers electrons from quinones to the beta subunit. EcoCyc product frame: NARI-MONOMER. EcoCyc synonyms: chlI. Genomic coordinates: 1285849-1286526. EcoCyc protein note: The γ subunit (NarI) of nitrate reductase A is a membrane-embedded heme-iron subunit resembling cytochrome b, which transfers electrons from the quinone pool to the β subunit (NarH). There are two hemes present, a low-potential heme bL and a high-potential heme bH . Electrons are thought to transfer from the quinol binding site (Q-site) via heme bL and heme bH to the [3Fe-4S] cluster of NarH . The Q-site of Nar is periplasmically oriented . NarI contains 5 transmembrane helices; the first helix appears to facilitate dimer formation. A C-terminal tail interacts with both NarG and NarH. The two Fe atoms are coordinated by histidine groups - His 56 and His 205 coordinate heme bH, His66 and His 187 coordinate heme bL. NarI contains an elongated hydrophobic cavity which may provide a protected interaction site for quinones . Reviews:

## Biological Role

Activated by fnr (protein.P0A9E5), narL (protein.P0AF28).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11350|protein.P11350]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=narI; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=narI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004125,ECOCYC:EG10640,GeneID:945808`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1285849-1286526:+; feature_type=gene
