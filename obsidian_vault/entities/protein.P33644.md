---
entity_id: "protein.P33644"
entity_type: "protein"
name: "yfiH"
source_database: "UniProt"
source_id: "P33644"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yfiH b2593 JW2575"
---

# yfiH

`protein.P33644`

## Static

- Type: `protein`
- Source: `UniProt:P33644`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Purine nucleoside enzyme that catalyzes the phosphorolysis of adenosine and inosine nucleosides, yielding D-ribose 1-phosphate and the respective free bases, adenine and hypoxanthine (PubMed:31978345). Also catalyzes the phosphorolysis of S-methyl-5'-thioadenosine into adenine and S-methyl-5-thio-alpha-D-ribose 1-phosphate (PubMed:31978345). Also has adenosine deaminase activity (PubMed:31978345). May also act as a polyphenol oxidase: able to oxidize syringaldazine and 2,2'-azino-bis(3-ethylbenzthiazoline-6-sulfonic acid) (ABTS) in vitro (PubMed:16740638). {ECO:0000269|PubMed:16740638, ECO:0000269|PubMed:31978345}. YfiH is a purine nucleoside phosphorylase; in vitro activity was tested with adenosine, S-methyl-5'-thioadenosine and inosine. The enzyme can also act as an adenosine deaminase . Earlier research showed that YfiH is a multicopper oxidase with polyphenol oxidase activity. Cyclic voltammetry measurements show that YfiH is a laccase with low redox potential . A yfiH deletion strain is more sensitive to ampicillin, cephradine and cephoxitin than wild type . Overexpression of LSERINEDEAM1-MONOMER SdaA or deletion of EG12142 sdaC suppresses the β-lactam sensitivity . A cell morphology-altering mutation was mapped to yfiH...

## Biological Role

Catalyzes guanosine:phosphate alpha-D-ribosyltransferase (reaction.R02147), purine-deoxynucleoside:phosphate ribosyltransferase (reaction.R10244), 5-METHYLTHIOADENOSINE-PHOSPHORYLASE-RXN (reaction.ecocyc.5-METHYLTHIOADENOSINE-PHOSPHORYLASE-RXN), ADENODEAMIN-RXN (reaction.ecocyc.ADENODEAMIN-RXN), ADENPHOSPHOR-RXN (reaction.ecocyc.ADENPHOSPHOR-RXN), INOPHOSPHOR-RXN (reaction.ecocyc.INOPHOSPHOR-RXN), RXN-16312 (reaction.ecocyc.RXN-16312).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Purine nucleoside enzyme that catalyzes the phosphorolysis of adenosine and inosine nucleosides, yielding D-ribose 1-phosphate and the respective free bases, adenine and hypoxanthine (PubMed:31978345). Also catalyzes the phosphorolysis of S-methyl-5'-thioadenosine into adenine and S-methyl-5-thio-alpha-D-ribose 1-phosphate (PubMed:31978345). Also has adenosine deaminase activity (PubMed:31978345). May also act as a polyphenol oxidase: able to oxidize syringaldazine and 2,2'-azino-bis(3-ethylbenzthiazoline-6-sulfonic acid) (ABTS) in vitro (PubMed:16740638). {ECO:0000269|PubMed:16740638, ECO:0000269|PubMed:31978345}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.R02147|reaction.R02147]] `KEGG` `database` - via EC:2.4.2.1
- `catalyzes` --> [[reaction.R10244|reaction.R10244]] `KEGG` `database` - via EC:2.4.2.1
- `catalyzes` --> [[reaction.ecocyc.5-METHYLTHIOADENOSINE-PHOSPHORYLASE-RXN|reaction.ecocyc.5-METHYLTHIOADENOSINE-PHOSPHORYLASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ADENODEAMIN-RXN|reaction.ecocyc.ADENODEAMIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ADENPHOSPHOR-RXN|reaction.ecocyc.ADENPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.INOPHOSPHOR-RXN|reaction.ecocyc.INOPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-16312|reaction.ecocyc.RXN-16312]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2593|gene.b2593]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33644`
- `KEGG:ecj:JW2575;eco:b2593;ecoc:C3026_14370;`
- `GeneID:947089;`
- `GO:GO:0000270; GO:0004000; GO:0004731; GO:0005507; GO:0005829; GO:0016682; GO:0017061; GO:0030288; GO:0042803`
- `EC:1.10.3.-; 2.4.2.1; 2.4.2.28; 3.5.4.4`

## Notes

Purine nucleoside phosphorylase YfiH (EC 2.4.2.1) (Adenosine deaminase YfiH) (EC 3.5.4.4) (Polyphenol oxidase YfiH) (EC 1.10.3.-) (S-methyl-5'-thioadenosine phosphorylase YfiH) (EC 2.4.2.28)
