---
entity_id: "protein.P76241"
entity_type: "protein"
name: "nimR"
source_database: "UniProt"
source_id: "P76241"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nimR yeaM b1790 JW1779"
---

# nimR

`protein.P76241`

## Static

- Type: `protein`
- Source: `UniProt:P76241`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Negatively regulates expression of the nimT operon and its own expression. Acts by binding to the nimR-nimT intergenic region. {ECO:0000269|PubMed:25790494}. NimR, formerly called YeaM, belongs to the AraC/XylS superfamily . It confers resistance to 2-nitroimidazole, an antibacterial and antifungal agent . NimR plays a regulatory role in divergent transcription of the nimT and nimR genes . Genome-wide NimR binding sites were determined in vivo by chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium . A negative correlation between cellular growth and the copy number of the proteins NimR has been reported . NimR: regulator of nimT . The NimR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Annotation

FUNCTION: Negatively regulates expression of the nimT operon and its own expression. Acts by binding to the nimR-nimT intergenic region. {ECO:0000269|PubMed:25790494}.

## Outgoing Edges (2)

- `represses` --> [[gene.b1790|gene.b1790]] `RegulonDB` `C` - regulator=NimR; target=nimR; function=-
- `represses` --> [[gene.b1791|gene.b1791]] `RegulonDB` `C` - regulator=NimR; target=nimT; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1790|gene.b1790]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76241`
- `KEGG:ecj:JW1779;eco:b1790;ecoc:C3026_10205;`
- `GeneID:946590;`
- `GO:GO:0003677; GO:0003700; GO:0006355; GO:0043565; GO:0045892`

## Notes

HTH-type transcriptional regulator NimR (Regulator of nimT)
