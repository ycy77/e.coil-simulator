---
entity_id: "protein.P0AGJ7"
entity_type: "protein"
name: "trmL"
source_database: "UniProt"
source_id: "P0AGJ7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01885}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trmL yibK b3606 JW3581"
---

# trmL

`protein.P0AGJ7`

## Static

- Type: `protein`
- Source: `UniProt:P0AGJ7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01885}.

## Enriched Summary

FUNCTION: Methylates the ribose at the nucleotide 34 wobble position in the two leucyl isoacceptors tRNA(Leu)(CmAA) and tRNA(Leu)(cmnm5UmAA). Catalyzes the methyl transfer from S-adenosyl-L-methionine to the 2'-OH of the wobble nucleotide. Recognition of the target requires a pyridine at position 34 and N(6)-(isopentenyl)-2-methylthioadenosine at position 37. {ECO:0000255|HAMAP-Rule:MF_01885, ECO:0000269|PubMed:20855540}. TrmL is the methyltransferase responsible for 2'-O-methylation of the wobble nucleotide 34 (cytidine or uridine) ribose in both tRNALeu isoacceptors . It also 2'-O-methylates a minor fraction of 5-methoxycarbonylmethoxy-modified U34 of serT-tRNA . TrmL showed no methyltransferase activity with certain synthetic tRNA substrates ; the enzyme requires the presence of the ms2i6 modification at the A37 nucleotide for activity . In addition, the A35 nucleotide functions as an identity element for substrate recognition by TrmL . TrmL only accepts pyrimidine nucleotides at the wobble position; additional identity elements within the anticodon loop were identified . TrmL belongs to the SPOUT superfamily of methyltransferases and is a dimer in solution . Crystal structures of the enzyme have been solved, allowing the identification of the SAM co-substrate binding site and the predicted active site...

## Biological Role

Component of tRNA (cytidine/uridine-2'-O)-ribose methyltransferase (complex.ecocyc.CPLX0-7421).

## Annotation

FUNCTION: Methylates the ribose at the nucleotide 34 wobble position in the two leucyl isoacceptors tRNA(Leu)(CmAA) and tRNA(Leu)(cmnm5UmAA). Catalyzes the methyl transfer from S-adenosyl-L-methionine to the 2'-OH of the wobble nucleotide. Recognition of the target requires a pyridine at position 34 and N(6)-(isopentenyl)-2-methylthioadenosine at position 37. {ECO:0000255|HAMAP-Rule:MF_01885, ECO:0000269|PubMed:20855540}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7421|complex.ecocyc.CPLX0-7421]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3606|gene.b3606]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGJ7`
- `KEGG:ecj:JW3581;eco:b3606;ecoc:C3026_19555;`
- `GeneID:948119;`
- `GO:GO:0002131; GO:0002132; GO:0003723; GO:0005737; GO:0042803; GO:0141098; GO:0141102`
- `EC:2.1.1.207`

## Notes

tRNA (cytidine(34)-2'-O)-methyltransferase (EC 2.1.1.207) (tRNA (cytidine/uridine-2'-O-)-methyltransferase TrmL)
