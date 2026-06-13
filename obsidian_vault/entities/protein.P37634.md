---
entity_id: "protein.P37634"
entity_type: "protein"
name: "rlmJ"
source_database: "UniProt"
source_id: "P37634"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rlmJ yhiR b3499 JW3466"
---

# rlmJ

`protein.P37634`

## Static

- Type: `protein`
- Source: `UniProt:P37634`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Specifically methylates the adenine in position 2030 of 23S rRNA. Nascent 23S rRNA seems to be the natural substrate. Appears to be not necessary for ribosome assembly. Required for the utilization of extracellular DNA as the sole source of carbon and energy (PubMed:11591672, PubMed:16707682). {ECO:0000255|HAMAP-Rule:MF_00934, ECO:0000269|PubMed:11591672, ECO:0000269|PubMed:16707682, ECO:0000269|PubMed:22847818, ECO:0000269|PubMed:23945937}. RlmJ is the methyltransferase responsible for methylation of 23S rRNA at the N6 position of the A2030 nucleotide. In vitro, RlmJ can methylate A2030 most efficiently in free 23S rRNA, but not in assembled 50S ribosomal subunits . Lack of RlmJ does not affect ribosome assembly. The abundance of only a limited number of proteins is affected by lack of 23S rRNA modification at A2030 . Crystal structures of the enzyme have been solved, allowing the identification of substrate binding sites. Site-directed mutagenesis of predicted active site residues confirmed their importance . rlmJ is a homologue of the H. influenzae competence gene comJ. A mutant with a defect in this gene is unable to utilize DNA as a sole carbon or energy source, despite retaining the ability to be artificially induced to competence...

## Biological Role

Catalyzes RXN0-6998 (reaction.ecocyc.RXN0-6998).

## Annotation

FUNCTION: Specifically methylates the adenine in position 2030 of 23S rRNA. Nascent 23S rRNA seems to be the natural substrate. Appears to be not necessary for ribosome assembly. Required for the utilization of extracellular DNA as the sole source of carbon and energy (PubMed:11591672, PubMed:16707682). {ECO:0000255|HAMAP-Rule:MF_00934, ECO:0000269|PubMed:11591672, ECO:0000269|PubMed:16707682, ECO:0000269|PubMed:22847818, ECO:0000269|PubMed:23945937}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6998|reaction.ecocyc.RXN0-6998]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3499|gene.b3499]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37634`
- `KEGG:ecj:JW3466;eco:b3499;ecoc:C3026_18950;`
- `GeneID:948012;`
- `GO:GO:0003723; GO:0005829; GO:0008988; GO:0015976; GO:0036307; GO:0070475`
- `EC:2.1.1.266`

## Notes

Ribosomal RNA large subunit methyltransferase J (EC 2.1.1.266) (23S rRNA (adenine(2030)-N6)-methyltransferase) (23S rRNA m6A2030 methyltransferase)
